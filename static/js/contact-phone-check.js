document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contacto');

  if (!form) return;

  let allowSubmit = false;

  form.addEventListener('submit', function (e) {
    if (allowSubmit) return;  // Permite enviar si ya se aceptó

    const phoneInput = form.querySelector('input[name="phone"]');
    if (phoneInput && phoneInput.value.trim() === '') {
      e.preventDefault(); // Detiene envío
      document.getElementById('customPhoneAlert').classList.remove('d-none');
    }
  });

  // Botón OMITIR → envía el formulario
  window.omitPhone = function () {
    document.getElementById('customPhoneAlert').classList.add('d-none');
    allowSubmit = true;
    form.submit(); // Ahora sí se envía
  };

  // Botón AGREGAR NÚMERO → solo enfoca el campo, no envía
  window.addPhone = function () {
    document.getElementById('customPhoneAlert').classList.add('d-none');
    form.querySelector('input[name="phone"]').focus();
  };
});
