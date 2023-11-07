// react-components.js

const Table = () => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Column 1</th>
                    <th>Column 2</th>
                    {/* Add more columns as needed */}
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Row 1, Column 1</td>
                    <td>Row 1, Column 2</td>
                    {/* Add more rows and data as needed */}
                </tr>
                {/* Add more rows as needed */}
            </tbody>
        </table>
    );
};

// Render the Table component to the root element in your HTML
ReactDOM.render(<Table />, document.getElementById('root'));
 