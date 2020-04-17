import {Component, OnInit} from '@angular/core';
import {Company} from '../models';
import {CompanyService} from '../company.service';

@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[];

  constructor(private companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompaniesList();
  }

  getCompaniesList() {
    this.companyService.getCompanyList()
      .subscribe(companies => {
        this.companies = companies;
      });
  }

  deleteCategory(id) {
    this.companyService.deleteCompany(id).subscribe(res => {
      // this.categories = this.categories.filter(c => c.id != id);
      // this.getCategoryList();
    });
  }

}