const { spawn } = require('child_process');
let child; 

function gestease(command) {
    if(command == 'start'){
        console.log('starting geastease');
        child = spawn('python', ['../python_scripts/speechrec.py', "start"]);

        child.stdout.on('data', function (data) {
            console.log("Python response: ", data.toString('utf8'));
            result.textContent = data.toString('utf8');
        });
        
        child.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
        });
        child.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
        });
    }else if(command == 'stop'){
        console.log('stopping gestease');
        child.kill('SIGTERM');
    }
}

module.exports = gestease;