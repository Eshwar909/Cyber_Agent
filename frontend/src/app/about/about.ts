import { Component } from '@angular/core';
import { Header } from './header/header';
import { RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [Header, RouterLink,RouterLinkActive],
  templateUrl: './about.html',
  styleUrl: './about.css',
})
export class About {}
