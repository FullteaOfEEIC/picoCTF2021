
 function solve(){
 	history.back();
 	console.log(history.state);
 	setTimeout(solve,1000);
 }

solve()

//picoCTF{th4ts_k1nd4_n34t_814c5bcf}
