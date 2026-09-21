(() => {
  // header con sombra al scrollear + WhatsApp flotante después del hero
  const hdr = document.getElementById("hdr");
  const flot = document.querySelector(".wa-flot");
  const onScroll = () => {
    const y = window.scrollY;
    hdr.classList.toggle("is-scroll", y > 8);
    if (flot) flot.classList.toggle("is-visible", y > 420);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // menú mobile
  const btn = document.getElementById("menu");
  const nav = document.getElementById("nav");
  const cerrar = () => {
    btn.setAttribute("aria-expanded", "false");
    btn.setAttribute("aria-label", "Abrir menú");
    nav.classList.remove("is-open");
  };
  btn.addEventListener("click", () => {
    const abierto = btn.getAttribute("aria-expanded") === "true";
    if (abierto) return cerrar();
    btn.setAttribute("aria-expanded", "true");
    btn.setAttribute("aria-label", "Cerrar menú");
    nav.classList.add("is-open");
  });
  nav.addEventListener("click", (e) => { if (e.target.closest("a")) cerrar(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") cerrar(); });

  // aparición suave
  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver((entradas) => {
      entradas.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    els.forEach((el) => io.observe(el));
  } else {
    els.forEach((el) => el.classList.add("is-in"));
  }

  // índice de temas: marca la sección visible
  const links = document.querySelectorAll(".temas__indice a");
  if (links.length && "IntersectionObserver" in window) {
    const porId = {};
    links.forEach((a) => { porId[a.getAttribute("href").slice(1)] = a; });
    const io2 = new IntersectionObserver((entradas) => {
      entradas.forEach((en) => {
        if (!en.isIntersecting) return;
        links.forEach((a) => a.classList.remove("is-activo"));
        const a = porId[en.target.id];
        if (a) a.classList.add("is-activo");
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    document.querySelectorAll(".tema").forEach((t) => io2.observe(t));
  }

  // formulario de contacto: arma el mensaje y abre WhatsApp (no se guarda nada)
  const form = document.getElementById("form-wa");
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const d = new FormData(form);
      const nombre = (d.get("nombre") || "").trim();
      const error = document.getElementById("form-error");
      if (!nombre) {
        error.hidden = false;
        form.nombre.focus();
        return;
      }
      error.hidden = true;
      const area = d.get("area");
      const detalle = (d.get("detalle") || "").trim();
      let msg = `Hola! Soy ${nombre}. Quisiera coordinar una entrevista ${d.get("modo")}`;
      msg += area ? ` por un tema de ${area.toLowerCase()}.` : ".";
      if (detalle) msg += `\n\n${detalle}`;
      window.open(`https://wa.me/${form.dataset.wa}?text=${encodeURIComponent(msg)}`, "_blank", "noopener");
    });
  }
})();
