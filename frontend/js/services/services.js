import {BASE_URL} from "../enviroments/enviroments.js";

export const getDepartamentos = async () => {
  const responde = await fetch(`${BASE_URL}/departamentos`);
  const json = await responde.json();
  return json;
};

export const postDepartamentos = async (departamento) => {
  const response = await fetch(`${BASE_URL}/departamentos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(departamento),
  });
  const json = await response.json();
  return json;
};

export const getDepartamento = async (id) => {
  const response = await fetch(`${BASE_URL}/departamento/${id}`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  });
  const json = await response.json();
  return json;
};

export const putDepartamento = async (departamento, id) => {
  const response = await fetch(`${BASE_URL}/departamento/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(departamento),
  });
  const json = await response.json();
  return json;
};

export const deleteDepartamento = async (id) => {
  const response = await fetch(`${BASE_URL}/departamento/${id}`, {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  });
  const json = await response.json();
  return json;
};
