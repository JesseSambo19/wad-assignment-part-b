const variable: number = 9;
const num1: number = 9;

const login = document.getElementById("login")!;

const logout = document.getElementById("logout")!;

login.addEventListener("click", () => {
  login.classList.add("none");
})

logout.addEventListener("click", () => {
  logout.classList.add("none");
  document.write("hi");
})

const none = () => {
  document.write("Hi");
} 