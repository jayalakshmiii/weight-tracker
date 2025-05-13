document.getElementById('weightForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const date = document.getElementById('date').value;
  const weight = document.getElementById('weight').value;

  if (!date || !weight) {
    alert('Please fill in all fields.');
    return;
  }

  const response = await fetch('/add', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ date, weight })
  });

  const result = await response.json();

  if (result.success) {
    window.location.reload();  // Refresh to see the updated table
  } else {
    alert('Failed to save entry.');
  }
});
