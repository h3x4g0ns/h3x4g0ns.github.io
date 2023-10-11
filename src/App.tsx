import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGithub, faLinkedin, faTwitter } from '@fortawesome/free-brands-svg-icons';
import './highlight.css';

interface AppProps {}

interface AppState {
  name: string;
  description: string;
  projects: { title: string; link: string; description: string }[];
  blogPosts: { title: string; link: string }[];
  socialLinks: { icon: any; link: string }[];
}

class App extends React.Component<AppProps, AppState> {
  constructor(props: AppProps) {
    super(props);
    this.state = {
      name: 'Your Name',
      description: 'A passionate developer specializing in web technologies.',
      projects: [
        {
          title: 'Project 1',
          link: 'https://project1.com',
          description: 'This is a description for Project 1.',
        },
        // ... add more projects as needed
      ],
      blogPosts: [
        {
          title: 'Blog Post 1',
          link: 'https://blogpost1.com',
        },
        // ... add more blog posts as needed
      ],
      socialLinks: [
        { icon: faGithub, link: 'https://github.com/yourusername' },
        { icon: faLinkedin, link: 'https://linkedin.com/in/yourusername' },
        { icon: faTwitter, link: 'https://twitter.com/yourusername' },
        // ... add more social links as needed
      ],
    };
  }

  render() {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-200 font-mono">
        <div className="bg-white p-8 rounded-lg shadow-md w-1/2">
          <h1 className="text-3xl font-bold mb-4 text-blue-600">{this.state.name}</h1>
          <p className="mb-6 text-gray-600">{this.state.description}</p>
          <h2 className="text-xl mb-2 text-blue-500">Projects:</h2>
          <ul className="mb-6">
            {this.state.projects.map((project, index) => (
              <li key={index} className="mb-2">
                <a href={project.link} className="text-blue-400 hover:underline">
                  {project.title}
                </a>
                <p className="text-gray-600">{project.description}</p>
              </li>
            ))}
          </ul>
          <h2 className="text-xl mb-2 text-blue-500">Blog Posts:</h2>
          <ul className="mb-6">
            {this.state.blogPosts.map((post, index) => (
              <li key={index} className="mb-1">
                <a href={post.link} className="text-blue-400 hover:underline">
                  {post.title}
                </a>
              </li>
            ))}
          </ul>
          <div className="flex space-x-4">
            {this.state.socialLinks.map((link, index) => (
              <a key={index} href={link.link} className="text-blue-500 hover:text-blue-600">
                <FontAwesomeIcon icon={link.icon} size="2x" />
              </a>
            ))}
          </div>
        </div>
      </div>
    );
  }
}

export default App;
