const fs = require("fs");

const main = async () => {
    fs.readFile("./brasileirao_serie_a.csv", "utf-8", (err, data) => {
        if (err){
            console.error("Error: ", err)
        }

        const linhas = data.split("\n");

        const times = linhas.map((coluna) => {
            return coluna.split(",")[7]
        })
        const times_sr = times.reduce((acc, curr) => {
            if(acc[curr]){
                return acc;
            } else {
                if(curr === undefined || curr === "time_mandante"){
                    return acc;
                }
                acc[curr] = curr;
                return acc;
            }
        }, {})

        fs.writeFile("depara_times.txt", Object.values(times_sr).toString().split(",").join(",\n").toString(), (err, data)=>{
            if(err){
                console.error("Err:", err);
            }
            console.log("success");
        })
    })

}

main();