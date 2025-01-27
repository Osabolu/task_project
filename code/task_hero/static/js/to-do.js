document.addEventListener("DOMContentLoaded", function () {  
    const popup = document.querySelector(".popup");
    const closeBtn = document.querySelector("#close");
    const overdueTasks = document.querySelectorAll(".tasks-card.overdue");

    // Check if the pop-up has been shown before
    const hasShownPopup = localStorage.getItem("popupShown");

    // Show pop-up only if there are overdue tasks and the pop-up hasn't been shown yet
    if (overdueTasks.length > 0 && !hasShownPopup) {
        // Show pop-up after 3 seconds
        setTimeout(function () {
            if (popup) {
                popup.classList.remove("hidden");
                // Mark the pop-up as shown
                localStorage.setItem("popupShown", "true");
            }
        }, 3000);
    }

    // Close the pop-up when the close button is clicked
    if (closeBtn) {
        closeBtn.addEventListener("click", function () {
            if (popup) {
                popup.classList.add("hidden");
            }
        });
    }
});



    document.addEventListener("DOMContentLoaded", function () {
        const themeToggle = document.getElementById("themeToggle");
        const themeLabel = document.getElementById("themeLabel");
        const body = document.body;

        // Load saved theme from localStorage
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme) {
            body.classList.add(savedTheme);
            themeToggle.checked = savedTheme === "dark-mode";
            themeLabel.textContent = savedTheme === "dark-mode" ? "Dark Mode" : "Light Mode";
        }

        // Toggle theme on switch change
        themeToggle.addEventListener("change", function () {
            if (themeToggle.checked) {
                body.classList.add("dark-mode");
                body.classList.remove("light-mode");
                localStorage.setItem("theme", "dark-mode");
                themeLabel.textContent = "Dark Mode";
            } else {
                body.classList.add("light-mode");
                body.classList.remove("dark-mode");
                localStorage.setItem("theme", "light-mode");
                themeLabel.textContent = "Light Mode";
            }
        });
    });





















  






