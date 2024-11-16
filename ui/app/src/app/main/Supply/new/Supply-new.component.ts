import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Supply-new',
  templateUrl: './Supply-new.component.html',
  styleUrls: ['./Supply-new.component.scss']
})
export class SupplyNewComponent {
  @ViewChild("SupplyForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}