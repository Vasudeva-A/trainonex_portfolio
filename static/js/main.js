document.addEventListener("DOMContentLoaded", function () {
  const revealItems = document.querySelectorAll(".reveal");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if ("IntersectionObserver" in window && revealItems.length && !reducedMotion) {
    document.body.classList.add("motion-ready");
    revealItems.forEach((item) => {
      const siblings = Array.from(item.parentElement.children)
        .filter((sibling) => sibling.classList.contains("reveal"));
      const delay = Math.min(siblings.indexOf(item), 5) * 70;
      item.style.setProperty("--reveal-delay", delay + "ms");
      item.classList.add("reveal-item");
    });
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else if (revealItems.length) {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  document.querySelectorAll("[data-password-toggle]").forEach((button) => {
    button.addEventListener("click", function () {
      const input = this.closest(".auth-password").querySelector("input");
      const showPassword = input.type === "password";
      input.type = showPassword ? "text" : "password";
      this.textContent = showPassword ? "Hide" : "Show";
      this.setAttribute("aria-label", showPassword ? "Hide password" : "Show password");
      this.setAttribute("aria-pressed", String(showPassword));
    });
  });

  const imageInput = document.querySelector("#id_cover_image");
  const imagePreview = document.querySelector("#imagePreview");
  const imagePreviewWrap = document.querySelector("#imagePreviewWrap");
  if (imageInput && imagePreview && imagePreviewWrap) {
    imageInput.addEventListener("change", function () {
      const file = this.files && this.files[0];
      if (!file) return;
      if (imagePreview.dataset.objectUrl) {
        URL.revokeObjectURL(imagePreview.dataset.objectUrl);
      }
      const objectUrl = URL.createObjectURL(file);
      imagePreview.dataset.objectUrl = objectUrl;
      imagePreview.src = objectUrl;
      imagePreview.alt = "Selected cover image preview";
      imagePreviewWrap.hidden = false;
    });
  }

  document.querySelectorAll("form[data-confirm]").forEach((form) => {
    form.addEventListener("submit", function (event) {
      if (!window.confirm(this.dataset.confirm)) {
        event.preventDefault();
      }
    });
  });

  document.querySelectorAll("form[data-submit-state]").forEach((form) => {
    form.addEventListener("submit", function () {
      const button = this.querySelector("[data-submit-label]");
      if (!button) return;
      button.disabled = true;
      button.setAttribute("aria-busy", "true");
      button.textContent = button.dataset.submitLabel;
    });
  });
});
