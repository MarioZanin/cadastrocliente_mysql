const API_URL = 'http://127.0.0.1:5000/clientes';
const form = document.getElementById('clientForm');
const tableBody = document.querySelector('#clientTable tbody');
const messageDiv = document.getElementById('message');

function showMessage(msg) {
    messageDiv.textContent = msg;
    setTimeout(() => messageDiv.textContent = '', 3000);
}

// READ (Carregar todos os clientes) - Colunas atualizadas
async function loadClients() {
    // ... lógica de fetch
    try {
        const response = await fetch(API_URL);
        const clients = await response.json();
        
        tableBody.innerHTML = ''; 

        clients.forEach(client => {
            const row = tableBody.insertRow();
            row.insertCell().textContent = client.id;
            row.insertCell().textContent = client.nome;
            row.insertCell().textContent = client.cpf; // Novo
            row.insertCell().textContent = client.email;
            row.insertCell().textContent = client.telefone;
            row.insertCell().textContent = client.endereco; // Novo
            
            // Botões de Ação
            const actionsCell = row.insertCell();
            const editButton = document.createElement('button');
            editButton.textContent = 'Editar';
            editButton.onclick = () => fillFormForEdit(client);
            
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Excluir';
            deleteButton.onclick = () => deleteClient(client.id);

            actionsCell.appendChild(editButton);
            actionsCell.appendChild(deleteButton);
        });
    } catch (error) {
        console.error('Erro ao carregar clientes:', error);
    }
}

// CREATE/UPDATE (Salvar cliente - POST ou PUT) - Campos atualizados
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const id = document.getElementById('clientId').value;
    const clientData = {
        nome: document.getElementById('nome').value,
        cpf: document.getElementById('cpf').value, // Novo
        email: document.getElementById('email').value,
        telefone: document.getElementById('telefone').value,
        endereco: document.getElementById('endereco').value // Novo
    };

    let url = API_URL;
    let method = 'POST';
    // ... lógica de switch POST/PUT
    if (id) {
        url = `${API_URL}/${id}`;
        method = 'PUT';
    }

    try {
        const response = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(clientData)
        });

        if (response.ok) {
            showMessage(`Cliente ${method === 'POST' ? 'Criado' : 'Atualizado'} com sucesso!`);
            resetForm();
            loadClients();
        } else {
            const errorData = await response.json();
            alert('Erro ao salvar cliente: ' + (errorData.message || 'Erro desconhecido.'));
        }
    } catch (error) {
        console.error('Erro de requisição:', error);
    }
});

// Função para preencher o formulário no modo Edição - Campos atualizados
function fillFormForEdit(client) {
    document.getElementById('clientId').value = client.id;
    document.getElementById('nome').value = client.nome;
    document.getElementById('cpf').value = client.cpf;
    document.getElementById('email').value = client.email;
    document.getElementById('telefone').value = client.telefone;
    document.getElementById('endereco').value = client.endereco;
}

// Função para limpar o formulário
function resetForm() {
    form.reset();
    document.getElementById('clientId').value = '';
}

// DELETE (Excluir Cliente)
async function deleteClient(id) {
    if (!confirm('Tem certeza que deseja excluir este cliente?')) return;
    // ... lógica de fetch DELETE
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            showMessage('Cliente excluído com sucesso!');
            loadClients();
        } else {
            alert('Erro ao excluir cliente.');
        }
    } catch (error) {
        console.error('Erro de requisição:', error);
    }
}

// Inicia o carregamento dos clientes ao carregar a página
document.addEventListener('DOMContentLoaded', loadClients);