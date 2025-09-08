n =  new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
h = n.getHours();
mm = n.getMinutes ();
s = n.getSeconds ();
document.getElementById("datetime").innerHTML = d + "." + m + "." + y +" / "+ h +":"+ mm +":"+ s;