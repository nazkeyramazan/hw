import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CompanyComponent} from './company/company.component';
import {VacancyComponent} from './vacancy/vacancy.component'

const routes: Routes = [
  { path: '', component: CompanyComponent },
  { path: 'company/:id/vacancies', component: VacancyComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
