displayItems();
const themeToggle = document.getElementById("themeToggle");
const currentTheme = localStorage.getItem("theme") || "light";

if (currentTheme === "dark") {
  document.body.classList.add("dark-mode");
  themeToggle.textContent = "☀️";
} else {
  document.body.classList.remove("dark-mode");
  themeToggle.textContent = "🌙";
}

themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const isDarkMode = document.body.classList.contains("dark-mode");
  themeToggle.textContent = isDarkMode ? "☀️" : "🌙";
  localStorage.setItem("theme", isDarkMode ? "dark" : "light");
});

function displayItems() {}
