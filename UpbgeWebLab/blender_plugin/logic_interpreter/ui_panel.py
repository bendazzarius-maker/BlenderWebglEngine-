"""Blender UI panel for logic brick export."""

from __future__ import annotations

import json
import os
from datetime import datetime

import bpy
from bpy.props import StringProperty
from bpy.types import Operator, Panel

from .export_runner import analyze_object_to_json_payload, get_js_module_for_object


class LB_OT_ChooseExportDir(Operator):
    bl_idname = "lb.choose_export_dir"
    bl_label = "Choose Folder"

    directory: StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        context.scene.lb_export_dir = self.directory
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class LB_OT_AnalyzeAndExport(Operator):
    bl_idname = "lb.analyze_export"
    bl_label = "Analyze & Export Selected"

    def execute(self, context):
        obj = context.active_object
        if obj is None:
            self.report({"ERROR"}, "No active object")
            return {"CANCELLED"}

        scene = context.scene
        if not scene.lb_export_dir:
            self.report({"ERROR"}, "Export directory not set")
            return {"CANCELLED"}

        payload = analyze_object_to_json_payload(obj)
        js_module = get_js_module_for_object(obj)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        basename = scene.lb_export_basename or "LB_Export"
        obj_name = obj.name
        os.makedirs(scene.lb_export_dir, exist_ok=True)
        json_path = os.path.join(scene.lb_export_dir, f"{basename}_{obj_name}_{ts}.json")
        js_path = os.path.join(scene.lb_export_dir, f"{basename}_{obj_name}_{ts}.js")
        with open(json_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
        with open(js_path, "w", encoding="utf-8") as fh:
            fh.write(js_module)
        text = bpy.data.texts.get(scene.lb_export_text_name) or bpy.data.texts.new(
            scene.lb_export_text_name
        )
        text.clear()
        text.write(js_module)
        self.report({"INFO"}, f"Exported to {json_path}")
        return {"FINISHED"}


class LB_PT_LogicExport(Panel):
    bl_space_type = "LOGIC_EDITOR"
    bl_region_type = "UI"
    bl_category = "LB Export"
    bl_label = "Logic Export"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.prop(scene, "lb_export_dir")
        layout.prop(scene, "lb_export_basename")
        layout.prop(scene, "lb_export_text_name")
        layout.operator("lb.choose_export_dir", text="Choose Folder")
        layout.operator("lb.analyze_export", text="Analyze & Export Selected")


classes = [LB_OT_ChooseExportDir, LB_OT_AnalyzeAndExport, LB_PT_LogicExport]


def register() -> None:
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.lb_export_dir = StringProperty(name="Export Dir", subtype="DIR_PATH")
    bpy.types.Scene.lb_export_basename = StringProperty(name="Base Name", default="LB_Export")
    bpy.types.Scene.lb_export_text_name = StringProperty(name="Text Name", default="LB_Export.js")


def unregister() -> None:
    for prop in ("lb_export_dir", "lb_export_basename", "lb_export_text_name"):
        if hasattr(bpy.types.Scene, prop):
            delattr(bpy.types.Scene, prop)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
