document.addEventListener("DOMContentLoaded", function() {
    const themeToggle = document.getElementById("themeToggle");
    const body = document.body;

    // Verifica e aplica o tema salvo no armazenamento local
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark");
        themeToggle.checked = true;
    }

    // Alterna o tema e salva a preferência
    themeToggle.addEventListener("change", () => {
        if (themeToggle.checked) {
            body.classList.add("dark");
            localStorage.setItem("darkMode", "enabled");
        } else {
            body.classList.remove("dark");
            localStorage.setItem("darkMode", "disabled");
        }
    });
});