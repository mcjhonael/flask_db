import {getDepartamentos,postDepartamentos,getDepartamento,putDepartamento,deleteDepartamento} from "./services/services.js"

let btnMostrar = document.getElementById("btnMostrar");
let btnActualizar = document.getElementById("btnActualizar");
let btnMostrar1 = document.getElementById("btnMostrar1");
let btnEliminar = document.getElementById("btnEliminar");
let mostrarContenido = document.getElementById("mostrarContenido");
let formulario = document.getElementById("formulario");
let inputNombre = document.getElementById("inputNombre");

btnMostrar.onclick=()=>{
    getDepartamentos().then((res)=>{
        console.log(res);
        paintDepartamentos(res)
    })
}

const paintDepartamentos=({content:departamentos})=>{
    mostrarContenido.textContent=""
    departamentos.forEach(objDepartamento => {
        const li=document.createElement("li")
        li.textContent=`${objDepartamento.nombre}`
        mostrarContenido.appendChild(li)
    });
}

formulario.onsubmit=(e)=>{
    e.preventDefault()
    if (inputNombre.value.length!=0){
        postDepartamentos({nombre:inputNombre.value}).then((res)=>{
            //aqui podemos colocar un mensaje de alerta de que fue exitoso
            console.log(res);
        })
    }
}

btnMostrar1.onclick=()=>{
    getDepartamento(3).then((res)=>{
        console.log(res);
        paintDepartamento(res);
    })
}

const paintDepartamento=({content:departamento})=>{
    mostrarContenido.textContent="";
    const li=document.createElement("li")
    li.textContent=`${departamento.nombre}`
    mostrarContenido.appendChild(li)
}
btnActualizar.onclick=()=>{
    putDepartamento({nombre:inputNombre.value},2).then((res)=>{
        console.log(res);
    })
}

//falta corregir la base de datos indicando el modo de eliminacion 
const eliminarDepartamento=()=>{
    deleteDepartamento(2)
}