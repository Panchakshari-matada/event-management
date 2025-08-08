const fetchStudents = async () => {
    const tableBody = document.querySelector('#student-table tbody');

    try {
        // Fetch the list of students from the backend
        const response = await fetch('http://127.0.0.1:8000/registers/');
        if (!response.ok) {
            throw new Error(`Failed to fetch students: ${response.statusText}`);
        }

        const students = await response.json();

        // Clear the table body
        tableBody.innerHTML = '';

        // Populate the table with student data
        students.forEach((student) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.email}</td>
                <td>${student.usn}</td>
                <td>${student.branch}</td>
                <td>${student.sem}</td>
                <td>${student.phone_number}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching students:', error);
        tableBody.innerHTML = '<tr><td colspan="7">Failed to load students. Please try again later.</td></tr>';
    }
};

// Fetch students when the page loads
fetchStudents();
