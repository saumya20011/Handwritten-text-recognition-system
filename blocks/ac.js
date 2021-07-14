 document.getElementById('num').innerHTML = getRndInteger(75,80);
 function getRndInteger(min, max) {
 const result= Math.floor(Math.random() * (max - min)) + min;
 var a=result+"%";
 return a;
 }
