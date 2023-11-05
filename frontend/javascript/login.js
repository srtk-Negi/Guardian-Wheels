const submitBtn = document.querySelector("btn1");

submitBtn.addEventListener("submit", function (e) {
  e.preventDefault();

  const userName = document.querySelector("userName").value;
  const password = document.querySelector("password").value;

  const formData = {
    userName: userName,
    password: password,
  };

  console.log(formData);
});
