import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Design-new',
  templateUrl: './Design-new.component.html',
  styleUrls: ['./Design-new.component.scss']
})
export class DesignNewComponent {
  @ViewChild("DesignForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}