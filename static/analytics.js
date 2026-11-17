(() => {
  const { site, goatcounter } = document.currentScript.dataset;
  const hostname = new URL(site).hostname;
  if (
    location.protocol !== "https:" ||
    ![hostname, `www.${hostname}`].includes(location.hostname) ||
    window.self !== window.top ||
    navigator.webdriver ||
    navigator.globalPrivacyControl ||
    [navigator.doNotTrack, window.doNotTrack].some((value) => ["1", "yes"].includes(value))
  ) {
    return;
  }

  const count = () => {
    if (document.visibilityState === "hidden") return;
    document.removeEventListener("visibilitychange", count);
    const url = new URL(goatcounter);
    url.search = new URLSearchParams({
      p: location.pathname,
      t: document.title,
      rnd: Math.random().toString(36).slice(2, 10),
    });
    fetch(url, {
      mode: "no-cors",
      credentials: "omit",
      referrerPolicy: "no-referrer",
      cache: "no-store",
      keepalive: true,
    }).catch(() => {});
  };

  document.addEventListener("visibilitychange", count);
  count();
})();
