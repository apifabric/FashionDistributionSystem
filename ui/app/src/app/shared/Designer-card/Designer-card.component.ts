import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Designer-card.component.html',
  styleUrls: ['./Designer-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Designer-card]': 'true'
  }
})

export class DesignerCardComponent {


}