
import { useEffect, useState } from 'react';
import { supabase } from '../utils/supabaseClient'; // Or Firebase client import
import { useForm } from 'react-hook-form';

const Home = () => {
  const [todos, setTodos] = useState([]);
  const { register, handleSubmit, reset } = useForm();

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    // Replace this with actual fetch logic from Supabase/Firebase
    const { data } = await supabase.from('todos').select('*');
    setTodos(data);
  };

  const onSubmit = async (data) => {
    // Call FastAPI endpoint to add todo
    await fetch('/api/add-todo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    fetchTodos();
    reset();
  };

  const handleDelete = async (id) => {
    await supabase.from('todos').delete().eq('id', id); // or Firebase delete logic
    fetchTodos();
  };

  return (
    <div>
      <h1>Todo App</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input {...register('title')} placeholder="New Todo" required />
        <button type="submit">Add</button>
      </form>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {todo.title}
            <button onClick={() => handleDelete(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
