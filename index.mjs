import fetch from "node-fetch";
import prompt from "prompt";
import dotenv from "dotenv";
dotenv.config();

async function query(data) {
    const response = await fetch(
        "https://api-inference.huggingface.co/models/ncoop57/DiGPTame-medium",
        {
            headers: { Authorization: `Bearer ${process.env.TOKEN}` },
            method: "POST",
            body: JSON.stringify(data),
        }
    );
    const result = await response.json();
    return result;
}

prompt.start();

function getText() {
    return new Promise((resolve, reject) => {
        prompt.get(["text"], (err, result) => {
            if (err) {
                reject(err);
            } else {
                resolve(result.text);
            }
        });
    });
}

async function chat() {
    while (true) {
        const text = await getText();
        const data = {
            text,            
        };
        const result = await query(data);
        console.log(result.generated_text);
    }
}

chat();









