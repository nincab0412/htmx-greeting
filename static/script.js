document.addEventListener("DOMContentLoaded", () => {
  document
    .querySelectorAll(".opacity-0")
    .forEach((el) => el.classList.add("opacity-100"));
});

const startBalloonAnimation = () => {
  gsap.to(".balloon", {
    y: () => -window.outerHeight - Math.random() * 100,
    x: () => `+=${Math.floor(Math.random() * 100) - 50}`,
    scale: () => Math.random() * 0.5 + 0.75,
    duration: () => Math.random() * 4 + 5,
    repeat: -1,
    ease: "power1.inOut",
    stagger: () => Math.random() * 2,
  });
};

const unhideImage = () => {
  document
    .querySelectorAll(".hide")
    .forEach((img) => img.classList.remove("invisible"));
};

document.addEventListener("DOMContentLoaded", startBalloonAnimation);
