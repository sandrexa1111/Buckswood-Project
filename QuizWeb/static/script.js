document.addEventListener("DOMContentLoaded", function () {
    const options = document.querySelectorAll("input[type='radio']");

    options.forEach(option => {
        option.addEventListener("change", function () {
            const parent = this.closest("div");
            parent.style.backgroundColor = "#00FF41";
            setTimeout(() => {
                parent.style.backgroundColor = "";
            }, 200);
        });
    });
});
