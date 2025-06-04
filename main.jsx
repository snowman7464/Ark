import React from 'react'
import ReactDOM from 'react-dom/client'

const App = () => (
  <div style={{ padding: '2em', fontFamily: 'sans-serif' }}>
    <h1>BreedTree ベータ版</h1>
    <p>これは開発中の恐竜ブリーディング管理アプリのベースです。</p>
  </div>
)

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
