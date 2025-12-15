window.addEventListener('DOMContentLoaded', function() {
  const dtInput = document.getElementById('alert-datetime');
  if (dtInput) {
    const now = new Date();
    // Format as "YYYY-MM-DDTHH:MM"
    const pad = n => n.toString().padStart(2, '0');
    const formatted = now.getFullYear() + '-' +
      pad(now.getMonth() + 1) + '-' +
      pad(now.getDate()) + 'T' +
      pad(now.getHours()) + ':' +
      pad(now.getMinutes());
    dtInput.min = formatted;
  }
  const recurringRadio = document.getElementById('recurring');
  const onetimeRadio = document.getElementById('onetime');
  const freqContainer = document.getElementById('frequency-container');

  function toggleFrequency() {
    if (recurringRadio.checked) {
      freqContainer.style.display = 'block';
    } else {
      freqContainer.style.display = 'none';
    }
  }

  recurringRadio.addEventListener('change', toggleFrequency);
  onetimeRadio.addEventListener('change', toggleFrequency);

  const form = document.querySelector('form[style*="flex-direction"]');
  if (!form) return;

  form.addEventListener('submit', function(e) {
    let valid = true;
    form.querySelectorAll('.input-error').forEach(el => el.classList.remove('input-error'));
    form.querySelectorAll('.error-message').forEach(el => el.remove());

    form.querySelectorAll('input[required], select[required]').forEach(input => {
      if (
        (input.type === 'radio' && !form.querySelector(`input[name="${input.name}"]:checked`)) ||
        (input.type !== 'radio' && !input.value.trim())
      ) {
        valid = false;
        input.classList.add('input-error');
        if (input.type === 'radio' && form.querySelector(`.error-message[data-for="${input.name}"]`)) return;
        const msg = document.createElement('div');
        msg.className = 'error-message';
        msg.textContent = 'This field is required.';
        if (input.type === 'radio') msg.setAttribute('data-for', input.name);
        input.parentNode.insertBefore(msg, input.nextSibling);
      }
    });

    if (!valid) {
      e.preventDefault();
      return;
    }

    // Prevent actual form submission
    e.preventDefault();

    // Gather form values
    const email = form.querySelector('#email-input').value;
    const runway = form.querySelector('#runway-select').value;
    const usage = form.querySelector('input[name="usage_type"]:checked').value;
    const datetime = form.querySelector('#alert-datetime').value;
    const alertType = form.querySelector('input[name="alert_type"]:checked').value;
    let frequencyText = '';
    if (alertType === 'Recurring') {
      const freqSelect = form.querySelector('#frequency-select');
      const freqValue = freqSelect.value;
      const freqLabel = freqSelect.options[freqSelect.selectedIndex].text;
      frequencyText = `every ${freqLabel}`;
    } else {
      frequencyText = 'One Time';
    }

    // Format datetime for display
    let displayDatetime = datetime.replace('T', ' ');

    // Create the message
    const msg = document.createElement('div');
    msg.style.marginTop = '20px';
    msg.style.background = '#e6f7ff';
    msg.style.padding = '12px';
    msg.style.borderRadius = '6px';
    msg.innerHTML = `
      Thank you for subscribing to runway alerts.<br>
      Your alert(s) would be sent to - <b>${email}</b><br>
      For Runway <b>${runway}</b> during <b>${usage}</b> usage.<br>
      from <b>${displayDatetime}</b> <b>${frequencyText}</b><br>
      Happy Spotting.
    `;

    // Remove any previous message
    const prevMsg = document.getElementById('runway-thankyou');
    if (prevMsg) prevMsg.remove();
    msg.id = 'runway-thankyou';

    // Insert after the form
    form.parentNode.insertBefore(msg, form.nextSibling);
  });
});
