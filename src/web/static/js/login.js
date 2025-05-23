function submitForm() {
    const usernameInput = document.querySelector("input#username-input");
    const passwordInput = document.querySelector("input#password-input");

    const body = {
        "username": usernameInput.value,
        "password": passwordInput.value
    };

    fetch(
        '/api/auth', {
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
        window.location.href = "/dashboard";
    })
    .catch(error => {
        console.error('Error:', error);
    });
}