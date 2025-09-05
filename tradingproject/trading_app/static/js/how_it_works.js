
document.addEventListener("DOMContentLoaded", () => {
  const container = document.querySelector(".timeline-container");
  const svgRef    = document.querySelector(".timeline-line"); // first curve SVG
  const steps     = document.querySelectorAll(".timeline-step");

  // Use the values you liked from the sliders
  const xs = [240, 520, 740, 960];
  const ys = [120, 440, 90, 480];

  function parseViewBox(svgEl) {
    const vb = svgEl.getAttribute("viewBox");   // e.g., "0 0 1436 276"
    if (!vb) return { w: svgEl.clientWidth, h: svgEl.clientHeight };
    const p = vb.trim().split(/\s+/).map(parseFloat);
    return { w: p[2], h: p[3] };
  }

  function placeAll() {
    const vb = parseViewBox(svgRef);
    const svgRect  = svgRef.getBoundingClientRect();
    const contRect = container.getBoundingClientRect();

    const scaleX = svgRect.width  / vb.w;
    const scaleY = svgRect.height / vb.h;

    steps.forEach((step, i) => {
      // convert viewBox coords to container pixels
      const xPx = (xs[i] * scaleX) + (svgRect.left - contRect.left);
      const yPx = (ys[i] * scaleY) + (svgRect.top  - contRect.top);

      step.style.left = xPx + "px";
      step.style.top  = yPx + "px";

      // fixed pattern: 1&3 below, 2&4 above
      if (i % 2 === 0) {         // 0,2
        step.classList.add("below");
        step.classList.remove("above");
      } else {                   // 1,3
        step.classList.add("above");
        step.classList.remove("below");
      }
    });
  }

  window.addEventListener("resize", placeAll);
  placeAll();
});

