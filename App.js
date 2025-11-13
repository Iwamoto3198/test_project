import React, { useState, useEffect } from 'react';

function App() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/todos')
      .then(response => response.json())
      .then(data => setTodos(data))
      .catch(() => setError('データ取得に失敗しました'));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://127.0.0.1:8000/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, completed: false })
    })
      .then(response => response.json())
      .then(data => {
        setTodos([...todos, data]);
        setTitle('');
        setError(null);
      })
      .catch(() => setError('TODO追加に失敗しました'));
  };

  const handleToggle = (id, completed) => {
    fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ completed: !completed })
    })
      .then(response => response.json())
      .then(data => {
        setTodos(todos.map(todo => 
          todo.id === id ? data : todo
        ));
      })
      .catch(() => setError('TODO更新に失敗しました'));
  };

  const handleDelete = (id) => {
    fetch(`http://127.0.0.1:8000/todos/${id}`, { method: 'DELETE' })
      .then(() => {
        setTodos(todos.filter(todo => todo.id !== id));
      })
      .catch(() => setError('TODO削除に失敗しました'));
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>TODOリスト</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="新しいTODOを入力"
          style={{ 
            width: '70%', 
            padding: '10px', 
            marginRight: '10px',
            fontSize: '16px'
          }}
        />
        <button 
          onClick={handleSubmit}
          disabled={!title.trim()}
          style={{ 
            padding: '10px 20px',
            fontSize: '16px',
            cursor: 'pointer'
          }}
        >
          追加
        </button>
      </div>

      <ul style={{ listStyle: 'none', padding: 0 }}>
        {todos.map((todo) => (
          <li 
            key={todo.id} 
            style={{ 
              marginBottom: '10px', 
              padding: '10px',
              border: '1px solid #ddd',
              borderRadius: '4px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', flex: 1 }}>
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => handleToggle(todo.id, todo.completed)}
                style={{ marginRight: '10px', cursor: 'pointer' }}
              />
              <span 
                style={{ 
                  textDecoration: todo.completed ? 'line-through' : 'none',
                  color: todo.completed ? '#888' : '#000'
                }}
              >
                {todo.title}
              </span>
            </div>
            <button 
              onClick={() => handleDelete(todo.id)}
              style={{ 
                padding: '5px 10px',
                backgroundColor: '#ff4444',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer'
              }}
            >
              削除
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;