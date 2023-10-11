import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import 'highlight.js/styles/github.css';

interface BlogPostProps {
  markdownContent: string;
}

const BlogPost: React.FC<BlogPostProps> = ({ markdownContent }) => {
  return (
    <div className="prose lg:prose-lg mx-auto p-4 bg-white rounded shadow">
      <ReactMarkdown 
        children={markdownContent} 
        remarkPlugins={[remarkGfm]} 
        components={{
          code({node, inline, className, children, ...props}) {
            const match = /language-(\w+)/.exec(className || '')
            return !inline && match ? (
              <pre className={className} {...props}>
                <code className={className}>
                  {children}
                </code>
              </pre>
            ) : (
              <code className={className} {...props}>
                {children}
              </code>
            )
          }
        }}
      />
    </div>
  );
}

export default BlogPost;
