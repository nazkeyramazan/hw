import {Component, OnInit} from '@angular/core';
import {Vacancy} from '../models';
import {CompanyService} from '../company.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  styleUrls: ['./vacancy.component.css']
})
export class VacancyComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private companyService: CompanyService,
              public route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getVacanciesList();
  }

  getVacanciesList() {
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.companyService.getVacancyList(id)
      .subscribe(vacancies => {
        this.vacancies = vacancies;
      });
  }

}