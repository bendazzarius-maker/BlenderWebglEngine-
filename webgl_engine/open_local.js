import { exec } from 'child_process';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const file = path.join(__dirname, 'index.html');

let command;
if (process.platform === 'win32') {
    command = `start "" "${file}"`;
} else if (process.platform === 'darwin') {
    command = `open "${file}"`;
} else {
    command = `xdg-open "${file}"`;
}

exec(command, err => {
    if (err) {
        console.error('Failed to open browser:', err);
    }
});
