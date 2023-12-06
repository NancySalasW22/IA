const numpeso=()=>{
    var p=document.querySelector("#pn").value;
    var ope=p/ 19.92;

    document.querySelector("#vpn").innerHTML=p;
    document.querySelector("#resultado").innerHTML="$"
    +ope.toFixed(2);


}   