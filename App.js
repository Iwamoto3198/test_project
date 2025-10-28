import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/posts')
      .then(response => setPosts(response.data))
      .catch(() => setError('データ取得に失敗しました'));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/posts', { title, body })
      .then(response => {
        setPosts([...posts, response.data]);
        setTitle('');
        setBody('');
        setError(null);
      })
      .catch(() => setError('投稿に失敗しました'));
  };

  return (
    <div>
      <h1>投稿一覧</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {posts.map((post, index) => (
        <div key={index}>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </div>
      ))}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="タイトル"
          required
        />
        <textarea
          value={body}
          onChange={(e) => setBody(e.target.value)}
          placeholder="本文"
          required
        />
        <button type="submit">投稿する</button>
      </form>
    </div>
  );
}

export default App;