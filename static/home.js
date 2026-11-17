const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

document.querySelectorAll("video[data-autoplay]").forEach((video) => {
  const updatePlayback = () => {
    if (reducedMotion.matches) {
      video.pause();
    } else {
      video.play().catch(() => video.pause());
    }
  };

  updatePlayback();
  reducedMotion.addEventListener("change", updatePlayback);
});
