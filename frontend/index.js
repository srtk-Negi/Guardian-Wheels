"use strict";
document.getElementById("personForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const details = document.getElementById("details").value;

  const formData = {
    name: name,
    details: details,
  };

  const jsonData = JSON.stringify(formData);

  // fetch("backend_url", {
  //   method: "POST",
  //   body: jsonData,
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  // })
  //   .then((response) => response.json())
  //   .then((data) => {
  //     document.getElementById("result").innerHTML =
  //       "Data sent to the backend: " + JSON.stringify(data);
  //   })
  //   .catch((error) => {
  //     document.getElementById("result").innerHTML = "Error: " + error;
  //   });
});
