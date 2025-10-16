const name = "太郎";
const age = 25;
const height = 170.5;
const isStudent = false;

console.log(`名前: ${name}, 年齢: ${age}, 身長: ${height} cm, 学生か？ ${isStudent}`);

function greet(name, age) {
    return `こんにちは、${name}さん！${age}歳！`;
}


const score = 90;

if (score >= 80) {
  console.log("合格！");
} else if (score >= 50) {
  console.log("補習が必要です");
} else {
  console.log("不合格…");
}

let fruits = ["りんご", "バナナ", "さくらんぼ"]
console.log(fruits[2])