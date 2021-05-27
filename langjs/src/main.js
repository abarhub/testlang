

var last = 0;

function randomNumber(max) {
    last = (25214903917 * last + 11) % 281474976710656;
    let tmp = (last >= 0) ? last : -last;
    return tmp % max;
}

function createArray(len, maxValue) {
    let p_array = new Array(len);
    for (let i = 0; i < len; i++) {
        p_array[i] = randomNumber(maxValue);
    }
    return p_array;
}

function main() {

    let tabSize = 10000000;
    let maxValue = 5000000;
    let noOutput = false;
    let debug = false;


    process.argv.forEach((val, index) => {
        if (val == "--nooutput") {
            noOutput = true;
        } else if (val.startsWith("--nbop=")) {
            let nb = parseInt(val.substring(7));
            if (nb > 0) {
                tabSize = nb;
            }
        } else if (val == "--debug") {
            debug = true;
        }
    });

    let tab = createArray(tabSize, maxValue);

    tab.sort();

    if (debug) {
        const util = require('util');
        process.argv.forEach((val, index) => {
            console.log(`   argv[${index}] : ${val}`);
        });
        console.log(util.format("lang=javascript;tabSize=%d;maxValue=%d;noOutput=%d;debug=%d\n",
            tabSize, maxValue, noOutput, debug));
    }

    if (!noOutput) {
        console.log("tableau : \n" + tab.slice(0, 10) + (tab.length > 10 ? " ..." : ""));
    }


}

main();
