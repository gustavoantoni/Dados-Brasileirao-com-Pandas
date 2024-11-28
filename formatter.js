/* 
* Feito por @gustavoantoni @figueiredojoaopedro @BL7Ki
* Script para filtrar os nomes dos times e ter cada nome de cada time distinto em um txt.
*/

const fs = require("fs");

const main = async () => {

    // lê o arquivo no repositorio em utf-8
    fs.readFile("./brasileirao_serie_a.csv", "utf-8", (err, data) => {
        // caso tenha erro, interrompe o fluxo
        if (err){
            console.error("Error: ", err);
            return;
        }

        // cada elemento do array é uma linha txt
        const linhas = data.split("\n");

        // divide cada coluna separada por vírgula (csv file)
        const times = linhas.map((coluna) => {
            return coluna.split(",")[7]
        })

        // reduce para pegar todos os times de modo distinto
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

        // escreve o arquivo com todos os times de modo distinto.
        fs.writeFile("depara_times.txt", Object.values(times_sr).toString().split(",").join(",\n").toString(), (err, data)=>{
            if(err){
                console.error("Err:", err);
            }
            console.log("success");
        })
    })

}

main();