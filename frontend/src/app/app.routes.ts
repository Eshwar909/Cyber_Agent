import { Routes } from '@angular/router';
import {About} from './about/about';
import {Llm} from './llm/llm';

export const routes: Routes = [
  { path: '', component: About },
  { path: 'llm', component: Llm }
];
