const showElement = ($el) => $el.style.display = ''
const hideElement = ($el) => $el.style.display = 'none'

const addClass = ($el, className) => $el.classList.add(className)
const removeClass = ($el, className) => $el.classList.remove(className)

/* Script for register */
const plan = document.getElementById('id_plan');
const cupon = document.getElementById('id_coupon');

if (plan !== null && cupon !== null) {
  showElement(cupon);
  hideElement(plan);

  const toggle = document.getElementById('customSwitch3');

  window.addEventListener('DOMContentLoaded', () => {
    toggle.addEventListener('click', (ev) => {
      if (toggle.checked) {
        showElement(plan)
        hideElement(cupon)
      } else {
        showElement(cupon)
        hideElement(plan)
      }
    })
  });
}
/* end script for register */

/* Script for landing */
const toggleCost = document.getElementById('customSwitch1')

if (toggleCost !== null) {
  const costAnual = [...document.getElementsByClassName('anual')]
  const costMensual = [...document.getElementsByClassName('mensual')]

  costMensual.forEach(hideElement)

  window.addEventListener('DOMContentLoaded', () => {
    toggleCost.addEventListener('click', () => {
      if (toggleCost.checked) {
        costAnual.forEach(hideElement)
        costMensual.forEach(showElement)
      } else {
        costAnual.forEach(showElement)
        costMensual.forEach(hideElement)
      }
    })
  });
}

/* end script for landing */
/* Script for register on select by id from landing */

const lastItem = ($arr) => $arr[$arr.length - 1]
//This variable is for select id on the select for plans.
const planes = document.getElementById('id_plan');
// this variable is for make split on the url when come my id select on the plan on landing.
const urlParams = window.location.href.split('/');

/* So, here get the params from id on plans and for this moment put
the or select the plan for the client.
It's necessary for every plan select for the client.
*/
if (lastItem(urlParams) in [1, 2, 3, 4, 5]) {
  if(lastItem(urlParams) == 1){
    planes[0].removeAttribute('selected');
    planes['2'].selected = true;
  }else if(lastItem(urlParams) == 2){
    planes[0].removeAttribute('selected');
    planes['3'].selected = true;
  }else if(lastItem(urlParams) == 3){
    planes[0].removeAttribute('selected');
    planes['4'].selected = true;
  }
}

/* end script for register */
