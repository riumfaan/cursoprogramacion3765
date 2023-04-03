var nombre = "Andres Umaña"
var edad = 39
var estatura = 160


document.write("hola")

var datos = document.getElementById("datos")

datos.innerHTML= `
  <h2>Hola soy datos</h2>
  <h3>Mi nombre: ${nombre}</h3>
  <h3>Estatura: ${edad}</h3>
`;

//SENTENCIAS CONDICIONALES

if(estatura >=150)
{
  datos.innerHTML += "<h1>Eres una persona ALTA</h1>";
}
else
{
  datos.innerHTML += "<h1>Eres una persona CHAPARRA</h1>";
}

for(var i = 2000; i<2023; i++)
{
  datos.innerHTML += "<h2>Estamos en el año </h2>" + i;
}
  
