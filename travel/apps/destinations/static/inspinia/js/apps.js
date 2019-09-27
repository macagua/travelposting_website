/* Script for register */
const showElement = ($el) => $el.style.display = ''
const hideElement = ($el) => $el.style.display = 'none'

const plan = document.getElementById('id_plan');
const cupon = document.getElementById('id_coupon');

showElement(plan);
hideElement(cupon);

const toggle = document.getElementById('toggle');

window.addEventListener('DOMContentLoaded', () => {
  toggle.addEventListener('click', (ev) => {
    if (toggle.checked) {
      showElement(cupon)
      hideElement(plan)
    } else {
      showElement(plan)
      hideElement(cupon)
    }
  })
});

/* end script for register */