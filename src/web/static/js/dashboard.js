function logoutDashboard() {
    fetch(
        '/api/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
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