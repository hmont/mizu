function submitForm() {
    const usernameInput = document.querySelector("input#username-input");
    const passwordInput = document.querySelector("input#password-input");

    const body = {
        "username": usernameInput.value,
        "password": passwordInput.value
    };

    fetch(
        '/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
    )
    .then(response => {
        if (!response.ok) {
          throw new Error('HTTP error! status: ${response.status}');
        }
        return response.json();
    })
    .then(responseData => {
        alert(responseData.message)
    })
    .catch(error => {
        console.error('Error:', error);
    });
}